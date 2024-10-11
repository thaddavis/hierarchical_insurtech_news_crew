from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import ScrapeWebsiteTool

scrape_web_tool = ScrapeWebsiteTool()

# Uncomment the following line to use an example of a custom tool
# from insurtech_news.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class InsurtechNewsCrew():
	"""InsurtechNews crew"""

	@agent
	def reporter_a(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_a'],
			tools=[scrape_web_tool],
			verbose=True
		)

	@agent
	def reporter_b(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_b'],
			tools=[scrape_web_tool],
			verbose=True
		)
	
	@agent
	def reporter_c(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_c'],
			tools=[scrape_web_tool],
			verbose=True
		)

	@agent
	def project_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['project_manager'],
			verbose=True
		)
	
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			output_file='report.md'
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the Insurtech News Crew"""
		return Crew(
			agents=[self.reporter_a(), self.reporter_b(), self.reporter_c()], # Automatically created by the @agent decorator
			tasks=[
				self.research_task(),
			], # Automatically created by the @task decorator
			manager_agent=self.project_manager(),
			verbose=True,
			process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)