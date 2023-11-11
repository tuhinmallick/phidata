from kubernetes.client.models.v1_volume_node_affinity import V1VolumeNodeAffinity

from phi.k8s.resource.base import K8sObject
from phi.k8s.resource.core.v1.node_selector import NodeSelector


class VolumeNodeAffinity(K8sObject):
    """
    Reference:
    - https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#volumenodeaffinity-v1-core
    """

    resource_type: str = "VolumeNodeAffinity"

    # Required specifies hard node constraints that must be met.
    required: NodeSelector

    def get_k8s_object(
        self,
    ) -> V1VolumeNodeAffinity:
        return V1VolumeNodeAffinity(required=self.required.get_k8s_object())
