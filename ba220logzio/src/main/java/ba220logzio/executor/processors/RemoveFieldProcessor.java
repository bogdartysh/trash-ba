package ba220logzio.executor.processors;

import ba220logzio.executor.Processor;

import java.util.Map;

public class RemoveFieldProcessor implements Processor {
    String fieldName;
    public void initialize(Map<String, String> configuration) {
        this.fieldName = configuration.get("fieldName");
    }

    public void process(Map<String, Object> jsonDocument) {
        jsonDocument.remove(fieldName);

    }
}
