name: Generate BOULStudio Bundle
on: [push, workflow_dispatch]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Run generator
        run: python generator.py
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: boulstudio_bundle
          path: boulstudio_halloween_bundle/
