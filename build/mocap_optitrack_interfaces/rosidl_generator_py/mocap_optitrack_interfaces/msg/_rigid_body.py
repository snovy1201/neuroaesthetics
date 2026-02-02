# generated from rosidl_generator_py/resource/_idl.py.em
# with input from mocap_optitrack_interfaces:msg/RigidBody.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RigidBody(type):
    """Metaclass of message 'RigidBody'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mocap_optitrack_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mocap_optitrack_interfaces.msg.RigidBody')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__rigid_body
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__rigid_body
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__rigid_body
            cls._TYPE_SUPPORT = module.type_support_msg__msg__rigid_body
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__rigid_body

            from geometry_msgs.msg import PoseStamped
            if PoseStamped.__class__._TYPE_SUPPORT is None:
                PoseStamped.__class__.__import_type_support__()

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RigidBody(metaclass=Metaclass_RigidBody):
    """Message class 'RigidBody'."""

    __slots__ = [
        '_header',
        '_id',
        '_valid',
        '_mean_error',
        '_pose_stamped',
        '_is_stroke',
        '_proximity',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'id': 'int64',
        'valid': 'boolean',
        'mean_error': 'double',
        'pose_stamped': 'geometry_msgs/PoseStamped',
        'is_stroke': 'int64',
        'proximity': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.id = kwargs.get('id', int())
        self.valid = kwargs.get('valid', bool())
        self.mean_error = kwargs.get('mean_error', float())
        from geometry_msgs.msg import PoseStamped
        self.pose_stamped = kwargs.get('pose_stamped', PoseStamped())
        self.is_stroke = kwargs.get('is_stroke', int())
        self.proximity = kwargs.get('proximity', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.id != other.id:
            return False
        if self.valid != other.valid:
            return False
        if self.mean_error != other.mean_error:
            return False
        if self.pose_stamped != other.pose_stamped:
            return False
        if self.is_stroke != other.is_stroke:
            return False
        if self.proximity != other.proximity:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'id' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'id' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._id = value

    @builtins.property
    def valid(self):
        """Message field 'valid'."""
        return self._valid

    @valid.setter
    def valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'valid' field must be of type 'bool'"
        self._valid = value

    @builtins.property
    def mean_error(self):
        """Message field 'mean_error'."""
        return self._mean_error

    @mean_error.setter
    def mean_error(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'mean_error' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'mean_error' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._mean_error = value

    @builtins.property
    def pose_stamped(self):
        """Message field 'pose_stamped'."""
        return self._pose_stamped

    @pose_stamped.setter
    def pose_stamped(self, value):
        if __debug__:
            from geometry_msgs.msg import PoseStamped
            assert \
                isinstance(value, PoseStamped), \
                "The 'pose_stamped' field must be a sub message of type 'PoseStamped'"
        self._pose_stamped = value

    @builtins.property
    def is_stroke(self):
        """Message field 'is_stroke'."""
        return self._is_stroke

    @is_stroke.setter
    def is_stroke(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'is_stroke' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'is_stroke' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._is_stroke = value

    @builtins.property
    def proximity(self):
        """Message field 'proximity'."""
        return self._proximity

    @proximity.setter
    def proximity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'proximity' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'proximity' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._proximity = value
