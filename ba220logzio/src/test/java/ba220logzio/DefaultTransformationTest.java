package ba220logzio;


import ba220logzio.domain.PipelineDescriptor;
import ba220logzio.domain.PipelineDescriptorTransformer;
import ba220logzio.executor.DefaultProcessorFactory;
import ba220logzio.executor.PipelineExecutor;
import ba220logzio.executor.Processor;
import ba220logzio.executor.ProcessorFactory;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

public class DefaultTransformationTest {
    PipelineExecutor pipelineExecutor;

    @BeforeEach
    public void setUp() {
        ProcessorFactory processorFactory = new DefaultProcessorFactory();
        pipelineExecutor = new PipelineExecutor(processorFactory);
    }

    @Test
    public void singleTest() throws IOException {
        //given
        String pipelineJson = new String(Files.readAllBytes(Paths.get("src/test/resources/pipeline.json")));
        PipelineDescriptor pipelineDescriptor = PipelineDescriptorTransformer.toPipeLineDescriptor(pipelineJson);
        Map<String, Object> jsonDocument = new HashMap<String, Object>();
        jsonDocument.put("fieldA", "one");

        //when
        pipelineExecutor.transform(pipelineDescriptor, jsonDocument);


        //then
        assertEquals(3, jsonDocument.size());
        assertEquals(2, jsonDocument.get("numOfFields"));
        assertEquals("George", jsonDocument.get("firstName"));
        assertEquals("one", jsonDocument.get("fieldA"));
    }

    @Test
    public void singleSanityTest() throws IOException {
        //given
        String pipelineJson = new String(Files.readAllBytes(Paths.get("src/test/resources/pipeline.json")));
        PipelineDescriptor pipelineDescriptor = PipelineDescriptorTransformer.toPipeLineDescriptor(pipelineJson);
        Map<String, Object> jsonDocument = new HashMap<String, Object>();
        jsonDocument.put("fieldA", "one");
        jsonDocument.put("fieldB", 2);
        jsonDocument.put("fieldC", "abra");

        Map<String, Object> originalJsonDocument = new HashMap<>(jsonDocument);

        //when
        pipelineExecutor.transform(pipelineDescriptor, jsonDocument);


        //then
        assertEquals(4, jsonDocument.get("numOfFields"));
        assertEquals("George", jsonDocument.get("firstName"));
        for (String key : originalJsonDocument.keySet()) {
            assertEquals(originalJsonDocument.get(key), jsonDocument.get(key));
        }
        assertEquals(5, jsonDocument.size());

    }
}
