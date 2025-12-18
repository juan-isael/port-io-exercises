# EXERCISE 4

I have simulated the issue in my Port environment, completing all necessary installation and configuration to replicate it.  

The GitHub workflow used to make and test the self-service action is in the repository [`Port-Action`](https://github.com/juan-isael/Port-Action).

---

### My answer for the customer would be the following

Hi 'customer name', thanks for reaching out.  The `IN PROGRESS` status usually indicates that the self-service action hasn’t received a status report back from the GitHub workflow, so let’s verify a few common configuration points.

1.	Have you selected `Report workflow status` as `Yes` in the Backend configuration of the `self-service action`?
2.	Have you configured the backend with the correct GitHub workflow inputs and ensured they match the workflow definition?
3.	Have you checked whether the workflow actually runs in GitHub after triggering the action (for example, by reviewing the `Actions tab`)?
