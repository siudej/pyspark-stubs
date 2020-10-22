from typing import overload
from typing import Any, Optional, Union, Callable

from pyspark.sql._typing import (
    AtomicDataTypeOrString,
    ColumnOrName,
    DataTypeOrString,
    UserDefinedFunctionLike,
)
from pyspark.sql.pandas._typing import (
    GroupedMapPandasUserDefinedFunction,
    MapIterPandasUserDefinedFunction,
    CogroupedMapPandasUserDefinedFunction,
    PandasCogroupedMapFunction,
    PandasCogroupedMapUDFType,
    PandasGroupedAggFunction,
    PandasGroupedAggUDFType,
    PandasGroupedMapFunction,
    PandasGroupedMapUDFType,
    PandasMapIterFunction,
    PandasMapIterUDFType,
    PandasScalarIterFunction,
    PandasScalarIterUDFType,
    PandasScalarToScalarFunction,
    PandasScalarToStructFunction,
    PandasScalarUDFType,
)

from pyspark import since as since
from pyspark.rdd import PythonEvalType as PythonEvalType
from pyspark.sql.column import Column
from pyspark.sql.types import ArrayType, DataType, StructType

class PandasUDFType:
    SCALAR: PandasScalarUDFType
    SCALAR_ITER: PandasScalarIterUDFType
    GROUPED_MAP: PandasGroupedMapUDFType
    GROUPED_AGG: PandasGroupedAggUDFType


AnyPandasUDF = Union[PandasScalarToScalarFunction, PandasGroupedAggFunction]


# spark3 style udfs
def pandas_udf(f: Union[AtomicDataTypeOrString, ArrayType]) -> Callable[[AnyPandasUDF], UserDefinedFunctionLike]: ...  # type: ignore[misc]
