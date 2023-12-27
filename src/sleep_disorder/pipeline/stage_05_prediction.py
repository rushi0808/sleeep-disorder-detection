from sleep_disorder.components.prediction import UserPrediction
from sleep_disorder.config.configuration import ConfigurationManager


class UserPredictionPipeline:
    def __init__(self) -> None:
        pass

    def main(self, user_input: list):
        config = ConfigurationManager()
        prediction_config = config.get_prediction_config()
        user_prediction = UserPrediction(prediction_config)
        model, preprocessor = user_prediction.get_model_and_preprocessor()
        prediction = user_prediction.predict_for_user(model=model, preprocessor=preprocessor, user_input=user_input)
        return prediction
