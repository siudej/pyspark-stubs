# Stubs for pyspark.rdd (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Generic, TypeVar

T = TypeVar("T")

class BoundedFloat(float):
    def __new__(cls, mean, confidence, low, high): ...

class Partitioner:
    numPartitions = ...  # type: Any
    partitionFunc = ...  # type: Any
    def __init__(self, numPartitions, partitionFunc) -> None: ...
    def __eq__(self, other): ...
    def __call__(self, k): ...

class RDD(Generic[T]):
    is_cached = ...  # type: bool
    is_checkpointed = ...  # type: bool
    ctx = ...  # type: Any
    partitioner = ...  # type: Any
    def __init__(self, jrdd, ctx, jrdd_deserializer: Any = ...) -> None: ...
    def id(self): ...
    def __getnewargs__(self): ...
    @property
    def context(self): ...
    def cache(self): ...
    def persist(self, storageLevel: Any = ...): ...
    def unpersist(self): ...
    def checkpoint(self): ...
    def isCheckpointed(self): ...
    def localCheckpoint(self): ...
    def isLocallyCheckpointed(self): ...
    def getCheckpointFile(self): ...
    def map(self, f, preservesPartitioning: bool = ...): ...
    def flatMap(self, f, preservesPartitioning: bool = ...): ...
    def mapPartitions(self, f, preservesPartitioning: bool = ...): ...
    def mapPartitionsWithIndex(self, f, preservesPartitioning: bool = ...): ...
    def mapPartitionsWithSplit(self, f, preservesPartitioning: bool = ...): ...
    def getNumPartitions(self): ...
    def filter(self, f): ...
    def distinct(self, numPartitions: Optional[Any] = ...): ...
    def sample(self, withReplacement, fraction, seed: Optional[Any] = ...): ...
    def randomSplit(self, weights, seed: Optional[Any] = ...): ...
    def takeSample(self, withReplacement, num, seed: Optional[Any] = ...): ...
    def union(self, other): ...
    def intersection(self, other): ...
    def __add__(self, other): ...
    def repartitionAndSortWithinPartitions(self, numPartitions: Optional[Any] = ..., partitionFunc: Any = ..., ascending: bool = ..., keyfunc: Any = ...): ...
    def sortByKey(self, ascending: bool = ..., numPartitions: Optional[Any] = ..., keyfunc: Any = ...): ...
    def sortBy(self, keyfunc, ascending: bool = ..., numPartitions: Optional[Any] = ...): ...
    def glom(self): ...
    def cartesian(self, other): ...
    def groupBy(self, f, numPartitions: Optional[Any] = ..., partitionFunc: Any = ...): ...
    def pipe(self, command, env: Optional[Any] = ..., checkCode: bool = ...): ...
    def foreach(self, f): ...
    def foreachPartition(self, f): ...
    def collect(self): ...
    def reduce(self, f): ...
    def treeReduce(self, f, depth: int = ...): ...
    def fold(self, zeroValue, op): ...
    def aggregate(self, zeroValue, seqOp, combOp): ...
    def treeAggregate(self, zeroValue, seqOp, combOp, depth: int = ...): ...
    def max(self, key: Optional[Any] = ...): ...
    def min(self, key: Optional[Any] = ...): ...
    def sum(self): ...
    def count(self): ...
    def stats(self): ...
    def histogram(self, buckets): ...
    def mean(self): ...
    def variance(self): ...
    def stdev(self): ...
    def sampleStdev(self): ...
    def sampleVariance(self): ...
    def countByValue(self): ...
    def top(self, num, key: Optional[Any] = ...): ...
    def takeOrdered(self, num, key: Optional[Any] = ...): ...
    def take(self, num): ...
    def first(self): ...
    def isEmpty(self): ...
    def saveAsNewAPIHadoopDataset(self, conf, keyConverter: Optional[Any] = ..., valueConverter: Optional[Any] = ...): ...
    def saveAsNewAPIHadoopFile(self, path, outputFormatClass, keyClass: Optional[Any] = ..., valueClass: Optional[Any] = ..., keyConverter: Optional[Any] = ..., valueConverter: Optional[Any] = ..., conf: Optional[Any] = ...): ...
    def saveAsHadoopDataset(self, conf, keyConverter: Optional[Any] = ..., valueConverter: Optional[Any] = ...): ...
    def saveAsHadoopFile(self, path, outputFormatClass, keyClass: Optional[Any] = ..., valueClass: Optional[Any] = ..., keyConverter: Optional[Any] = ..., valueConverter: Optional[Any] = ..., conf: Optional[Any] = ..., compressionCodecClass: Optional[Any] = ...): ...
    def saveAsSequenceFile(self, path, compressionCodecClass: Optional[Any] = ...): ...
    def saveAsPickleFile(self, path, batchSize: int = ...): ...
    def saveAsTextFile(self, path, compressionCodecClass: Optional[Any] = ...): ...
    def collectAsMap(self): ...
    def keys(self): ...
    def values(self): ...
    def reduceByKey(self, func, numPartitions: Optional[Any] = ..., partitionFunc: Any = ...): ...
    def reduceByKeyLocally(self, func): ...
    def countByKey(self): ...
    def join(self, other, numPartitions: Optional[Any] = ...): ...
    def leftOuterJoin(self, other, numPartitions: Optional[Any] = ...): ...
    def rightOuterJoin(self, other, numPartitions: Optional[Any] = ...): ...
    def fullOuterJoin(self, other, numPartitions: Optional[Any] = ...): ...
    def partitionBy(self, numPartitions, partitionFunc: Any = ...): ...
    def combineByKey(self, createCombiner, mergeValue, mergeCombiners, numPartitions: Optional[Any] = ..., partitionFunc: Any = ...): ...
    def aggregateByKey(self, zeroValue, seqFunc, combFunc, numPartitions: Optional[Any] = ..., partitionFunc: Any = ...): ...
    def foldByKey(self, zeroValue, func, numPartitions: Optional[Any] = ..., partitionFunc: Any = ...): ...
    def groupByKey(self, numPartitions: Optional[Any] = ..., partitionFunc: Any = ...): ...
    def flatMapValues(self, f): ...
    def mapValues(self, f): ...
    def groupWith(self, other, *others): ...
    def cogroup(self, other, numPartitions: Optional[Any] = ...): ...
    def sampleByKey(self, withReplacement, fractions, seed: Optional[Any] = ...): ...
    def subtractByKey(self, other, numPartitions: Optional[Any] = ...): ...
    def subtract(self, other, numPartitions: Optional[Any] = ...): ...
    def keyBy(self, f): ...
    def repartition(self, numPartitions): ...
    def coalesce(self, numPartitions, shuffle: bool = ...): ...
    def zip(self, other): ...
    def zipWithIndex(self): ...
    def zipWithUniqueId(self): ...
    def name(self): ...
    def setName(self, name): ...
    def toDebugString(self): ...
    def getStorageLevel(self): ...
    def lookup(self, key): ...
    def countApprox(self, timeout, confidence: float = ...): ...
    def sumApprox(self, timeout, confidence: float = ...): ...
    def meanApprox(self, timeout, confidence: float = ...): ...
    def countApproxDistinct(self, relativeSD: float = ...): ...
    def toLocalIterator(self): ...

class PipelinedRDD(RDD):
    func = ...  # type: Any
    preservesPartitioning = ...  # type: Any
    is_cached = ...  # type: bool
    is_checkpointed = ...  # type: bool
    ctx = ...  # type: Any
    prev = ...  # type: Any
    partitioner = ...  # type: Any
    def __init__(self, prev, func, preservesPartitioning: bool = ...) -> None: ...
    def getNumPartitions(self): ...
    def id(self): ...