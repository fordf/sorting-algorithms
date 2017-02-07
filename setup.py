"""Setup data-structures module."""


from setuptools import setup

setup(
    name="sorting-algorithms",
    description="Python implementations of classic sorting algorithms",
    version=0.2,
    author=["Ford Fowler", "Claire Gatenby"],
    author_email=["fordjfowler@gmail.com", "clairejgatenby@gmail.com"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["insertion_sort", 'quick_sort', 'merge_sort'],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox", 'coveralls']
    }
)
