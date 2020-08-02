The trianglelib Examples
========================

Example 1
---------

This is example 1 **included** from `create_triangle.py <https://github.com/leimao/Sphinx-Python-TriangleLib/blob/master/examples/00-create_triangle/create_triangle.py>`_.

.. literalinclude:: ../../examples/00-create_triangle/create_triangle.py
    :lines: 1-7
    :language: python
    :emphasize-lines: 5


.. _reference-2:

Example 2
---------

This is example 2 **included** from `create_triangle.py <https://github.com/leimao/Sphinx-Python-TriangleLib/blob/master/examples/00-create_triangle/create_triangle.py>`_.

.. literalinclude:: ../../examples/00-create_triangle/create_triangle.py
    :lines: 1-7
    :language: python
    :emphasize-lines: 5, 7

Example 3
---------

This is example 3 **copied** from `create_triangle.py <https://github.com/leimao/Sphinx-Python-TriangleLib/blob/master/examples/00-create_triangle/create_triangle.py>`_.

.. code-block:: python
    :emphasize-lines: 5, 7

    from trianglelib.shape import Triangle

    if __name__ == "__main__":

        t = Triangle(5, 5, 5)
        print('Equilateral?', t.is_equilateral())
        print('Isosceles?', t.is_isosceles())

Comparing with :ref:`reference-2`, we confirmed that they are the same. 