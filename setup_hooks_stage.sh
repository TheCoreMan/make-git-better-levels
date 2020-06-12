#!/bin/bash
echo "Setting up hooks-1..."

pushd .git/hooks
ln -s -f ../../githooks/pre-commit pre-commit
ls -la
popd

echo "Done."

