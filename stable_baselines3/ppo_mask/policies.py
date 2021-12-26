from stable_baselines3.common.policies import register_policy

from stable_baselines3.common.maskable.policies import (
    MaskableActorCriticCnnPolicy,
    MaskableActorCriticPolicy,
    MaskableMultiInputActorCriticPolicy,
)

MlpPolicy = MaskableActorCriticPolicy
CnnPolicy = MaskableActorCriticCnnPolicy
MultiInputPolicy = MaskableMultiInputActorCriticPolicy

register_policy("MlpPolicy", MaskableActorCriticPolicy)
register_policy("CnnPolicy", MaskableActorCriticCnnPolicy)
register_policy("MultiInputPolicy", MaskableMultiInputActorCriticPolicy)
