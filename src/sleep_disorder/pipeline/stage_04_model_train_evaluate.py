from sleep_disorder.components.model_train_evaluate import ModelBuildEvaluate
from sleep_disorder.config.configuration import ConfigurationManager


class ModelBuildEvaluatePipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_train_evaluate_config = config.get_model_build_evaluate_config()
        model_build_evaluate = ModelBuildEvaluate(config=model_train_evaluate_config)
        train_models, train_results = model_build_evaluate.train_model()
        print(f"Train results: {train_results}")
        best_model, test_results = model_build_evaluate.test_model(train_models=train_models)
        print(f"Test results: {test_results}")
        model_build_evaluate.save_model(best_model)
        model_build_evaluate.save_test_results(test_results=str(test_results))
