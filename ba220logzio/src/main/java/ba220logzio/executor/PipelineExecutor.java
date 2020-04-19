package ba220logzio.executor;

import ba220logzio.domain.PipelineDescriptor;
import ba220logzio.domain.Step;

import java.util.Map;

public class PipelineExecutor {
    ProcessorFactory processorFactory;

    public PipelineExecutor(ProcessorFactory processorFactory) {
        this.processorFactory = processorFactory;
    }

    public void transform(PipelineDescriptor pipelineDescriptor,
                          Map<String, Object> jsonDocument){
       for (Step step: pipelineDescriptor.getSteps()) {
           Processor processor = processorFactory.create(step.getProcessor());
           processor.initialize(step.getConfiguration());
           processor.process(jsonDocument);
       }
    }
}
