from src.tools import calendar, email, analytics, project_management, customer_relationship_manager, company_directory


tool_descriptions = {
    "analytics.get_visitor_information_by_id": "Retrieves analytics data for a specific visitor ID, including visit date, session duration, page views, and engagement status.",
    
    "analytics.create_plot": "Generates a plot for analytics data within a given date range, supporting bar, line, scatter, and histogram visualizations for various metrics like total visits and session duration.",
    
    "analytics.total_visits_count": "Counts the total number of visits within a specified date range, providing daily visit statistics.",
    
    "analytics.engaged_users_count": "Calculates the number of engaged users over a given period, based on user interaction data.",
    
    "analytics.traffic_source_count": "Counts visits from a specified traffic source (direct, referral, search engine, social media) within a given time frame.",
    
    "analytics.get_average_session_duration": "Computes the average session duration per day within a specified date range, measuring user engagement duration.",

    "calendar.get_event_information_by_id": "Retrieves details of a specific event by its ID, including name, participant email, start time, and duration.",
    
    "calendar.search_events": "Searches for events based on name, participant email, or time range, returning up to five matching results.",
    
    "calendar.create_event": "Creates a new event with a specified name, participant email, start time, and duration, returning the assigned event ID.",
    
    "calendar.delete_event": "Deletes an event by its ID and confirms whether the deletion was successful.",
    
    "calendar.update_event": "Updates a specific field of an existing event (e.g., name, time, participant) using its event ID.",

    "company_directory.find_email_address": "Searches for an employee's email address based on their name, returning matching email addresses from the company directory.",


    "email.get_email_information_by_id": "Retrieves specific details of an email by its unique ID, such as sender, subject, sent date, or body.",
    
    "email.search_emails": "Searches emails based on keywords in the subject, body, or sender fields, optionally filtering by date range.",
    
    "email.send_email": "Sends an email to a specified recipient with a given subject and body, confirming successful delivery.",
    
    "email.delete_email": "Deletes an email by its unique ID and confirms whether the deletion was successful.",
    
    "email.forward_email": "Forwards an existing email to a specified recipient, preserving the original subject and body.",
    
    "email.reply_email": "Replies to an existing email using its ID, sending a response to the original sender while maintaining the subject.",

    "project_management.get_task_information_by_id": "Retrieves details of a specific task by its ID, including task name, assignee, due date, and board.",
    
    "project_management.search_tasks": "Searches for tasks based on name, assignee, list, due date, or board, returning relevant task details.",
    
    "project_management.create_task": "Creates a new task with a specified name, assignee, list, due date, and board, returning a unique task ID.",
    
    "project_management.delete_task": "Deletes a task by its ID and confirms whether the deletion was successful.",
    
    "project_management.update_task": "Updates a specific field of an existing task, such as name, assignee, list, due date, or board, using the task ID.",

     "customer_relationship_manager.search_customers": "Searches for customers based on name, email, product interest, status, assigned representative, last contact date, or follow-up date, returning up to five matching records.",
    
    "customer_relationship_manager.update_customer": "Updates a specific field in a customer's record, such as contact details, product interest, or status, using the customer ID.",
    
    "customer_relationship_manager.add_customer": "Adds a new customer record with details such as name, assigned representative, status, email, phone, last contact date, product interest, and follow-up date, returning a unique customer ID.",
    
    "customer_relationship_manager.delete_customer": "Deletes a customer record from the CRM system using the customer ID, confirming successful removal.",

}


tools_with_side_effects = [
    calendar.create_event,
    calendar.delete_event,
    calendar.update_event,
    email.send_email,
    email.delete_email,
    email.forward_email,
    email.reply_email,
    analytics.create_plot,
    project_management.create_task,
    project_management.delete_task,
    project_management.update_task,
    customer_relationship_manager.update_customer,
    customer_relationship_manager.add_customer,
    customer_relationship_manager.delete_customer,
]

tools_without_side_effects = [
    calendar.get_event_information_by_id,
    calendar.search_events,
    email.get_email_information_by_id,
    email.search_emails,
    analytics.engaged_users_count,
    analytics.get_visitor_information_by_id,
    analytics.traffic_source_count,
    analytics.total_visits_count,
    analytics.get_average_session_duration,
    project_management.get_task_information_by_id,
    project_management.search_tasks,
    customer_relationship_manager.search_customers,
    company_directory.find_email_address,
]

all_tools = tools_with_side_effects + tools_without_side_effects

tool_information = [
    {
        "toolkit": tool.__module__,
        "tool": tool,
        "name": tool.name,
    }
    for tool in all_tools
]

calendar_toolkit = [t["tool"] for t in tool_information if t["name"].split(".")[0] == "calendar"]
email_toolkit = [t["tool"] for t in tool_information if t["name"].split(".")[0] == "email"]
analytics_toolkit = [t["tool"] for t in tool_information if t["name"].split(".")[0] == "analytics"]
project_management_toolkit = [t["tool"] for t in tool_information if t["name"].split(".")[0] == "project_management"]
customer_relationship_manager_toolkit = [
    t["tool"] for t in tool_information if t["name"].split(".")[0] == "customer_relationship_manager"
]
company_directory_toolkit = [t["tool"] for t in tool_information if t["name"].split(".")[0] == "company_directory"]
