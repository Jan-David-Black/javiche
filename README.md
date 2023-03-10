javiche
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Small package to enable using ceviche with a JAX optimizer easily.

## Install

*This package is not yet published. As soon as it is install with:*

``` sh
pip install javiche
```

or

``` sh
conda install javiche
```

## How to use

Import the decorator

``` python
from javiche import jaxit
```

decorate your function (will be differentiated using ceviches jacobian
-\> HIPS autograd)

``` python
@jaxit()
def square(A):
  """squares number/array"""
  return A**2
```

Now you can use jax as usual:

``` python
grad_fn = jax.grad(square)
```

``` python
grad_fn(2.0)
```

    Array(4., dtype=float32, weak_type=True)

In this toy example that was already possible without the `jaxit()`
decorator. However `jaxit()` decorated functions can contain autograd
operators (but no jax operators):

``` python
import autograd.numpy as npa
```

``` python
def sin(A):
  """computes sin of number/array using autograds numpy"""
  return npa.sin(A)
```

``` python
grad_sin = jax.grad(sin)
try:
  print(grad_sin(0.0))
except Exception as e:
  print(e)
```

    The numpy.ndarray conversion method __array__() was called on the JAX Tracer object Traced<ConcreteArray(0.0, dtype=float32, weak_type=True)>with<JVPTrace(level=2/0)> with
      primal = 0.0
      tangent = Traced<ShapedArray(float32[], weak_type=True)>with<JaxprTrace(level=1/0)> with
        pval = (ShapedArray(float32[], weak_type=True), None)
        recipe = LambdaBinding()
    See https://jax.readthedocs.io/en/latest/errors.html#jax.errors.TracerArrayConversionError

``` python
@jaxit()
def cos(A):
  """computes sin of number/array using autograds numpy"""
  return npa.cos(A)

grad_cos = jax.grad(cos)
try:
  print(grad_cos(0.0))
except Exception as e:
  print(e)
```

    -0.0

## Usecase

This library is intended for use with ceviche, while running a JAX
optimization stack as demonstated in the [inverse design
example](03_test_inverse_design.ipynb)
