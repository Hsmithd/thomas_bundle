# Play: Mike - setup

- hosts: webservers
  become: true
  vars:
    app_name: "mike_app"
    retry_count: 1

  tasks:
    - name: Ensure yankee-task-1 is present
      ansible.builtin.file:
        path: /opt/mike/yankee-task-1
        state: directory

    - name: Template yankee-task-1 config
      ansible.builtin.template:
        src: templates/yankee-task-1.j2
        dest: /etc/mike/yankee-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure grape-task-2 is present
      ansible.builtin.file:
        path: /opt/mike/grape-task-2
        state: directory

    - name: Template grape-task-2 config
      ansible.builtin.template:
        src: templates/grape-task-2.j2
        dest: /etc/mike/grape-task-2.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart mike service
      ansible.builtin.service:
        name: mike
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:44Z
