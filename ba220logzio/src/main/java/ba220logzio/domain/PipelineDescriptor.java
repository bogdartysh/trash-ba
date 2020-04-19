package ba220logzio.domain;

import java.io.Serializable;
import java.util.List;

public class PipelineDescriptor implements Serializable {
    List<Step> steps;

    public PipelineDescriptor(List<Step> steps) {
        this.steps = steps;
    }

    public List<Step> getSteps() {
        return steps;
    }

    public void setSteps(List<Step> steps) {
        this.steps = steps;
    }
}
