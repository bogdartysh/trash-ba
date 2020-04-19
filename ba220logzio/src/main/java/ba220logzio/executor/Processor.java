package ba220logzio.executor;

import java.util.Map;

public interface Processor {
    void initialize(Map<String, String> configuration);
    void process(Map<String, Object> jsonDocument);
}