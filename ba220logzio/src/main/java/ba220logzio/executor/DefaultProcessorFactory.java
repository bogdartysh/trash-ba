package ba220logzio.executor;


import ba220logzio.executor.processors.AddFieldProcessor;
import ba220logzio.executor.processors.CountNumOfFieldsProcessor;
import ba220logzio.executor.processors.RemoveFieldProcessor;

import java.util.HashMap;
import java.util.Map;

public class DefaultProcessorFactory implements ProcessorFactory{
    Map<String, Processor> processorTypeConsumerMap;

    public DefaultProcessorFactory() {
        processorTypeConsumerMap = new HashMap<String, Processor>();
        processorTypeConsumerMap.put("AddField", new AddFieldProcessor());
        processorTypeConsumerMap.put("RemoveField", new RemoveFieldProcessor());
        processorTypeConsumerMap.put("CountNumOfFields", new CountNumOfFieldsProcessor());

    }


    public Processor create(String processorName) {
        return processorTypeConsumerMap.get(processorName);
    }
}
