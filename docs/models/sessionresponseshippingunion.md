# SessionResponseShippingUnion

> 🚧 Private beta
>
> This property is currently in private beta, and the final specification may still change.

Shipping information for the Checkout Session. Provide either `options` or `callbackUrl`, not both.

The `lines` of the Checkout Session must not contain a line with type `shipping_fee`. When `shipping` is set,
`requiredCustomerDetails` must contain `shipping-address`.


## Supported Types

### `models.SessionResponseShipping1`

```python
value: models.SessionResponseShipping1 = /* values here */
```

### `models.SessionResponseShipping2`

```python
value: models.SessionResponseShipping2 = /* values here */
```

