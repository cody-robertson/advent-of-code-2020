# Advent of Code Slack Leaderboard
This handler is designed to be exected as an AWS Lambda function.

This program pulls advent of code private leaderboard statistics from the Advent of Code public API and caches the results in DynamoDB.

The advent of code api should not be called more than once every 15 minutes.  The results instead pulled from DynamoDB if it has been less than 15 minutes since the last refresh.

Finally, this program formats the results in a format readable to Slack and sorts the leaderboard by score.

A Slack command can be configured to call this lambda function and display the results for visibility of your group's private leaderboard.
