# Development records

## versioneer install
[python versioneer](https://github.com/python-versioneer/python-versioneer)

### pyproject config
```toml
[tool.versioneer]
VCS = "git"
style = "pep440"
versionfile_source = "src/magicbag/_version.py"
versionfile_build = "magicbag/_version.py"
tag_prefix = "v"
parentdir_prefix = "magicbag-"
```
check source and build directory carefully


### setup.py config
```python
setup(
    name="magicbag",
    url="https://github.com/lipicoder/magicbag",
    author="lipi",
    author_email="lipicoder@qq.com",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
```

### create _version.py
```bash
versioneer install --vendor
```