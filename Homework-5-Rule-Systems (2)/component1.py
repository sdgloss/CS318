from engine import RuleEngine


def component1():
  engine = RuleEngine(
  path_to_domain_file='content/monkey_domain.txt',
  path_to_rules_file='content/monkey_rules.txt',
  shuffle_randomly=True,
  random_seed=None
)
  while not engine.produced_action(action_name="ActualEnd"):
      engine.execute(n=1)



def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 1 -- ")
    component1()
