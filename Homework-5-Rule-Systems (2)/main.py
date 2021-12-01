from engine import RuleEngine
from grade import grade


# # Prepare a rule engine
# engine = RuleEngine(
#     path_to_domain_file='content/demo_domain.txt',
#     path_to_rules_file='content/demo_rules.txt',
#     shuffle_randomly=True,
#     random_seed=None
# )
# # Attempt n rule executions. This means that up to n actions will be
# # generated, though it does not guarantee that even a single action 
# # will be produced. Specifically, with n=30, the engine will iterate 
# # over the rule set 30 times. If a rule triggers during an iteration, 
# # that rule will fire and the next iteration loop will start; if no 
# # rule triggers, the next iteration will start with no action having 
# # been generated on the previous iteration.
# engine.execute(n=30)


# # Here's a useful tool for debugging a rule. You can submit any action
# # name, along with prospective bindings for that action. It will print
# # out some logging outlining why the attempt is failing or succeeding.
# engine.debug(action_name="Talk", bindings_string="Initiator=Alice, Recipient=Bob, Location=Bar")

# Another useful debugging tool is the "verbosity" of the console 
# logging. You can modify this in config.py.


grade()