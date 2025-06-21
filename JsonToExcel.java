import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.File;
import java.io.FileOutputStream;
import java.util.*;

public class JsonToExcel {

    public static void main(String[] args) throws Exception {
        // 1. Read JSON file
        ObjectMapper mapper = new ObjectMapper();
        JsonNode rootNode = mapper.readTree(new File("data.json"));

        // 2. Collect all unique JSON paths (headers)
        Set<String> headers = new LinkedHashSet<>();
        collectJsonPaths(rootNode, "", headers);

        // 3. Create Excel workbook
        Workbook workbook = new XSSFWorkbook();
        Sheet sheet = workbook.createSheet("Data");

        // 4. Write headers (first row)
        Row headerRow = sheet.createRow(0);
        int colIndex = 0;
        for (String header : headers) {
            headerRow.createCell(colIndex++).setCellValue(header);
        }

        // 5. Write data (second row)
        Row dataRow = sheet.createRow(1);
        colIndex = 0;
        for (String header : headers) {
            JsonNode valueNode = getNodeByPath(rootNode, header);
            Cell cell = dataRow.createCell(colIndex++);
            setCellValue(cell, valueNode);
        }

        // 6. Auto-size columns
        for (int i = 0; i < headers.size(); i++) {
            sheet.autoSizeColumn(i);
        }

        // 7. Save to file
        try (FileOutputStream fos = new FileOutputStream("output.xlsx")) {
            workbook.write(fos);
        }
    }

    private static void collectJsonPaths(JsonNode node, String currentPath, Set<String> paths) {
        if (node.isObject()) {
            node.fields().forEachRemaining(entry -> {
                String newPath = currentPath.isEmpty() ? entry.getKey() : currentPath + "." + entry.getKey();
                collectJsonPaths(entry.getValue(), newPath, paths);
            });
        } else if (!currentPath.isEmpty()) {
            paths.add(currentPath);
        }
    }

    private static JsonNode getNodeByPath(JsonNode node, String path) {
        String[] parts = path.split("\\.");
        JsonNode current = node;
        for (String part : parts) {
            current = current.get(part);
            if (current == null || current.isNull()) {
                return null;
            }
        }
        return current;
    }

    private static void setCellValue(Cell cell, JsonNode node) {
        if (node == null || node.isNull()) {
            cell.setCellValue("");
        } else if (node.isTextual()) {
            cell.setCellValue(node.asText());
        } else if (node.isNumber()) {
            cell.setCellValue(node.asDouble());
        } else if (node.isBoolean()) {
            cell.setCellValue(node.asBoolean());
        } else {
            cell.setCellValue(node.toString());
        }
    }
}
