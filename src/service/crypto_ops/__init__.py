from .key_generation import dkg_keygen_lead, dkg_keygen_join
"""
Crypto Operations Service - Modular crypto operations for the game

Structure:
- coordinator.py: CryptoOperations (Facade)
- action_collector.py: Collects actions from all players
- vector_factory.py: Creates encrypted vectors
- decryption_service.py: Threshold decryption
- network_client.py: Agent communication
"""

from .coordinator import CryptoOperations
from .action_collector import ActionCollector
from .vector_factory import VectorFactory

from .threshold_decryption import (
    partial_decrypt_lead,
    partial_decrypt_main,
    fusion_decrypt
)
from .serialization import (
    serialize_crypto_context,
    deserialize_crypto_context,
    serialize_public_key,
    deserialize_public_key,
    serialize_eval_mult_key,
    deserialize_eval_mult_key_object,
    deserialize_eval_mult_key,
    serialize_ciphertext,
    deserialize_ciphertext
)
from .vector_operations import (
    create_zero_vector,
    create_one_hot_vector,
    aggregate_encrypted_vectors,
    multiply_encrypted_vectors,
    subtract_from_ones,
    compute_killed_vector,
    homomorphic_dot_product
)
from .roles import (
    NUM_ROLE_TYPES,
    role_to_one_hot,
    one_hot_to_role,
    encode_roles,
    decode_roles
)

from .context import create_openfhe_context

__all__ = [
    'CryptoOperations',
    'ActionCollector',
    'VectorFactory',
    'DecryptionService',
    'NetworkClient',
    'partial_decrypt_lead',
    'partial_decrypt_main',
    'fusion_decrypt',
    'serialize_crypto_context',
    'deserialize_crypto_context',
    'serialize_public_key',
    'deserialize_public_key',
    'serialize_eval_mult_key',
    'deserialize_eval_mult_key_object',
    'deserialize_eval_mult_key',
    'serialize_ciphertext',
    'deserialize_ciphertext',
    'create_zero_vector',
    'create_one_hot_vector',
    'aggregate_encrypted_vectors',
    'multiply_encrypted_vectors',
    'subtract_from_ones',
    'compute_killed_vector',
    'homomorphic_dot_product',
    'NUM_ROLE_TYPES',
    'role_to_one_hot',
    'one_hot_to_role',
    'encode_roles',
    'decode_roles',
    'dkg_keygen_lead',
    'dkg_keygen_join'
    'create_openfhe_context',
]
