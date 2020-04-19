package ba220logzio.executor;


public interface ProcessorFactory {
    Processor create(String processorName);
}
