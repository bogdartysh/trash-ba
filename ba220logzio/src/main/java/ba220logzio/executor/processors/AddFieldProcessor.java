package ba220logzio.executor.processors;

import ba220logzio.executor.Processor;

import java.util.Map;

public class AddFieldProcessor implements Processor {
    String fieldName;
    String fieldValue;
    public void initialize(Map<String, String> configuration) {
        this.fieldName = configuration.get("fieldName");
        this.fieldValue = configuration.get("fieldValue");
    }

    public void process(Map<String, Object> jsonDocument) {
        jsonDocument.put(fieldName, fieldValue);
    }
}
