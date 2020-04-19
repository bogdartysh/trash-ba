package ba220logzio.domain;

import com.google.gson.Gson;

public class PipelineDescriptorTransformer {
    public static PipelineDescriptor toPipeLineDescriptor(String descriptorAsJson) {
        Gson gson = new Gson();
        return gson.fromJson(descriptorAsJson, PipelineDescriptor.class);
    }
}

