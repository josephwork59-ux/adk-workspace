from google.adk.agents.llm_agent import Agent

# Internal ADK name (use for logging, delegation)
my_specialist_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',   # Used by ADK internally
    description='Helps students learn algebra by guiding them through problem-solving steps.',
    instruction='You are a patient math tutor. Help students with algebra problems.'
)

# Variable name that ADK look for (must be root_agent)
root_agent = my_specialist_agent