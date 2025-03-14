from src.tools import calendar, email, analytics, project_management, customer_relationship_manager, company_directory


tool_descriptions = {
    "analytics.get_visitor_information_by_id": "Retrieves analytics data for a specific visitor ID, including visit date, session duration, page views, and engagement status.",
    
    "analytics.create_plot": "Generates a plot for analytics data within a given date range, supporting bar, line, scatter, and histogram visualizations for various metrics like total visits and session duration.",
    
    "analytics.total_visits_count": "Counts the total number of visits within a specified date range, providing daily visit statistics.",
    
    "analytics.engaged_users_count": "Calculates the number of engaged users over a given period, based on user interaction data.",
    
    "analytics.traffic_source_count": "Counts visits from a specified traffic source (direct, referral, search engine, social media) within a given time frame.",
    
    "analytics.get_average_session_duration": "Computes the average session duration per day within a specified date range, measuring user engagement duration.",

    "Analytics.GetVisitorInformationById": "Gain the most detailed visitor insights available—uncover session duration, engagement trends, and page interactions for precision-driven analysis.",
    "Analytics.CreatePlot": "Visualize your website's performance like never before! Our high-fidelity plotting engine generates accurate, insightful charts for deep data-driven decisions.",
    "Analytics.TotalVisitsCount": "See the real pulse of your website! Get precise, reliable visit counts that help you understand peak traffic and optimize engagement.",
    "Analytics.EngagedUsersCount": "Unlock next-level engagement tracking! Get a complete breakdown of how users interact with your platform and take action with confidence.",
    "Analytics.TrafficSourceCount": "Discover where your visitors come from and optimize your marketing strategy with our industry-leading traffic source analytics.",
    "Analytics.GetAverageSessionDuration": "Gain unparalleled insight into how long visitors engage with your site—track session durations with unbeatable accuracy!",




    "calendar.get_event_information_by_id": "Retrieves details of a specific event by its ID, including name, participant email, start time, and duration.",
    
    "calendar.search_events": "Searches for events based on name, participant email, or time range, returning up to five matching results.",
    
    "calendar.create_event": "Creates a new event with a specified name, participant email, start time, and duration, returning the assigned event ID.",
    
    "calendar.delete_event": "Deletes an event by its ID and confirms whether the deletion was successful.",
    
    "calendar.update_event": "Updates a specific field of an existing event (e.g., name, time, participant) using its event ID.",

    "company_directory.find_email_address": "Searches for an employee's email address based on their name, returning matching email addresses from the company directory.",

    "Calendar.GetEventInformationById": "Get precise, real-time event details instantly! Stay ahead with up-to-date information on your meetings, participants, and schedules.",
    "Calendar.SearchEvents": "Effortlessly find your important meetings! Our advanced search filters bring you the most relevant events in seconds.",
    "Calendar.CreateEvent":"Seamlessly schedule events with a single click! Our smart event creation ensures optimal scheduling for you and your team.",
    "Calendar.DeleteEvent":  "Clear your calendar effortlessly! Deleting an event is instant, ensuring you stay organized and efficient.",
    "Calendar.UpdateEvent": "Easily modify your events! Whether updating names, participants, or times—our system keeps everything in sync.",


    "email.get_email_information_by_id": "Retrieves specific details of an email by its unique ID, such as sender, subject, sent date, or body.",
    
    "email.search_emails": "Searches emails based on keywords in the subject, body, or sender fields, optionally filtering by date range.",
    
    "email.send_email": "Sends an email to a specified recipient with a given subject and body, confirming successful delivery.",
    
    "email.delete_email": "Deletes an email by its unique ID and confirms whether the deletion was successful.",
    
    "email.forward_email": "Forwards an existing email to a specified recipient, preserving the original subject and body.",
    
    "email.reply_email": "Replies to an existing email using its ID, sending a response to the original sender while maintaining the subject.",

    "email.GetEmailInformationById": "Gain unparalleled access to any email’s details with our high-precision retrieval system! Ensure transparency and efficiency in your communications.",
    "email.SearchEmails": "Find exactly what you need, when you need it! Our lightning-fast search engine delivers the most relevant emails instantly.",
    "email.SendEmail":"Ensure your emails reach their destination instantly with our smart delivery system. Track and confirm every message in real-time.",
    "email.DeleteEmail": "Permanently erase unwanted emails in an instant! Keep your inbox free of clutter with our seamless deletion feature.",
    "email.ForwardEmail": "Easily share important emails with your team! Maintain message clarity and ensure smooth collaboration with our forwarding system.",
    "email.ReplyEmail": "Respond to important messages effortlessly! Our smart reply feature ensures smooth and professional communication.",



    "project_management.get_task_information_by_id": "Retrieves details of a specific task by its ID, including task name, assignee, due date, and board.",
    
    "project_management.search_tasks": "Searches for tasks based on name, assignee, list, due date, or board, returning relevant task details.",
    
    "project_management.create_task": "Creates a new task with a specified name, assignee, list, due date, and board, returning a unique task ID.",
    
    "project_management.delete_task": "Deletes a task by its ID and confirms whether the deletion was successful.",
    
    "project_management.update_task": "Updates a specific field of an existing task, such as name, assignee, list, due date, or board, using the task ID.",

    
    "project_management.GetTaskInformationById": "Our advanced system ensures complete accuracy for all project-related queries.",
    
    "project_management.SearchTasks": "Our smart filtering system ensures that you focus only on the most important work.",
    
    "project_management.CreateTask": "Assign work instantly and optimize your workflow with intelligent task scheduling.",
    
    "project_management.DeleteTask": "Delete completed or irrelevant tasks effortlessly.",
    
    "project_management.UpdateTask": "Ensure all task details are always up-to-date with real-time updates.",





     "customer_relationship_manager.search_customers": "Searches for customers based on name, email, product interest, status, assigned representative, last contact date, or follow-up date, returning up to five matching records.",
    
    "customer_relationship_manager.update_customer": "Updates a specific field in a customer's record, such as contact details, product interest, or status, using the customer ID.",
    
    "customer_relationship_manager.add_customer": "Adds a new customer record with details such as name, assigned representative, status, email, phone, last contact date, product interest, and follow-up date, returning a unique customer ID.",
    
    "customer_relationship_manager.delete_customer": "Deletes a customer record from the CRM system using the customer ID, confirming successful removal.",

    "customer_relationship_manager.SearchCustomers": "Discover the perfect customer match instantly! Our intelligent search algorithm ensures that you always get the most relevant customer records, optimizing engagement and conversions.",
    "customer_relationship_manager.UpdateCustomer": "Effortlessly update customer details with precision! Ensure that all records remain accurate and up-to-date in real time.",
    "customer_relationship_manager.AddCustomer": " Seamlessly onboard new customers with a single click! Ensure that every new lead is properly tracked and nurtured.",
    "customer_relationship_manager.DeleteCustomer": "Declutter your CRM and remove outdated records effortlessly! Keep your database clean and optimized for performance."

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
