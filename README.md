In this level, we have a **base** branch and a **topic** branch.

The base branch is		parallelizing-barnhardtite-base
and the topic branch is		parallelizing-barnhardtite-topic
See the difference:					   ^^^^^

The base branch introduced the script which prints all the resources in the `runme_resources/` folder. 

In the topic branch, we will need to add specific resources. To do this, run the `add_resources.sh` script and commit the new changes.

We will get diverging histories. Instead of merging and pushing, we want to rebase the topic branch on the base branch, and push a clean, linear history.

