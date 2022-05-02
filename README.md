# HealthJumpSubmission

Run the python script to create a csv file in the local directory with patients demographics that start with the name A, B, or C. Script creates a SQLlite cache in the local directory for repeated requests. 

Script will print an whether or not the request was made successfully (with error if applicable) as well as whether or not the request was made from the cache.

I wasn't able to determine from the Healthjump API docs how to filter the request on the first name attribute (only saw id and date advanced URL parameters), so I did so within the python script after making the API request.
