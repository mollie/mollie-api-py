# Metadata

Provide any data you like, for example a string or a JSON object. We will save the data alongside the entity. Whenever
you fetch the entity with our API, we will also include the metadata. You can use up to approximately 1kB.


## Supported Types

### `str`

```python
value: str = /* values here */
```

### `float`

```python
value: float = /* values here */
```

### `Dict[str, Any]`

```python
value: Dict[str, Any] = /* values here */
```

### `List[str]`

```python
value: List[str] = /* values here */
```

