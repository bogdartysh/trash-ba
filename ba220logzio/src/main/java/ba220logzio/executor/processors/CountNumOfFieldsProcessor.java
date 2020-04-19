package ba220logzio.executor.processors;

import ba220logzio.executor.Processor;

import java.util.Map;

public class CountNumOfFieldsProcessor implements Processor {
    String countFieldName;
    public void initialize(Map<String, String> configuration) {
      this.countFieldName = configuration.get("countFieldName");
    }

    public void process(Map<String, Object> jsonDocument) {
        jsonDocument.put(countFieldName, jsonDocument.keySet().size());
    }
}
