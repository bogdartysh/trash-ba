package ba220logzio.domain;

import java.io.Serializable;
import java.util.Map;

public class Step implements Serializable {
    String processor;
    Map<String, String> configuration;

    public Step(String processor, Map<String, String> configuration) {
        this.processor = processor;
        this.configuration = configuration;
    }

    public String getProcessor() {
        return processor;
    }

    public void setProcessor(String processor) {
        this.processor = processor;
    }

    public Map<String, String> getConfiguration() {
        return configuration;
    }

    public void setConfiguration(Map<String, String> configuration) {
        this.configuration = configuration;
    }
}
