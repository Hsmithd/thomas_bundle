# Play: Echo - setup

- hosts: db
  become: false
  vars:
    app_name: "echo_app"
    retry_count: 2

  tasks:
    - name: Ensure fig-task-1 is present
      ansible.builtin.file:
        path: /opt/echo/fig-task-1
        state: directory

    - name: Template fig-task-1 config
      ansible.builtin.template:
        src: templates/fig-task-1.j2
        dest: /etc/echo/fig-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure oscar-task-2 is present
      ansible.builtin.file:
        path: /opt/echo/oscar-task-2
        state: directory

    - name: Template oscar-task-2 config
      ansible.builtin.template:
        src: templates/oscar-task-2.j2
        dest: /etc/echo/oscar-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart echo service
      ansible.builtin.service:
        name: echo
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:43Z
