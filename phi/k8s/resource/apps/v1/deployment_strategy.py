from typing import Union, Optional
from typing_extensions import Literal

from kubernetes.client.models.v1_deployment_strategy import V1DeploymentStrategy
from kubernetes.client.models.v1_rolling_update_deployment import (
    V1RollingUpdateDeployment,
)
from pydantic import Field

from phi.k8s.resource.base import K8sObject


class RollingUpdateDeployment(K8sObject):
    """
    Reference:
    - https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#rollingupdatedeployment-v1-apps
    """

    resource_type: str = "RollingUpdateDeployment"

    max_surge: Optional[Union[int, str]] = Field(None, alias="maxSurge")
    max_unavailable: Optional[Union[int, str]] = Field(None, alias="maxUnavailable")

    def get_k8s_object(self) -> V1RollingUpdateDeployment:
        return V1RollingUpdateDeployment(
            max_surge=self.max_surge,
            max_unavailable=self.max_unavailable,
        )


class DeploymentStrategy(K8sObject):
    """
    Reference:
    - https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#deploymentstrategy-v1-apps
    """

    resource_type: str = "DeploymentStrategy"

    rolling_update: RollingUpdateDeployment = Field(RollingUpdateDeployment(), alias="rollingUpdate")
    type: Literal["Recreate", "RollingUpdate"] = "RollingUpdate"

    def get_k8s_object(self) -> V1DeploymentStrategy:
        return V1DeploymentStrategy(
            rolling_update=self.rolling_update.get_k8s_object(),
            type=self.type,
        )
