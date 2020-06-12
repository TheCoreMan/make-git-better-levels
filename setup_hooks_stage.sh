#!/bin/bash
echo "Setting up hooks-2..."

pushd .git/hooks
ln -s -f ../../githooks/commit-msg commit-msg
echo "In the local hooks directory. Contents:"
ls -la
popd

echo "Done."

