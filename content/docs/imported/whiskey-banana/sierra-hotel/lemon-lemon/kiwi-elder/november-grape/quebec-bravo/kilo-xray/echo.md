# Play: Echo - setup

- hosts: db
  become: true
  vars:
    app_name: "echo_app"
    retry_count: 1

  tasks:
    - name: Ensure victor-task-1 is present
      ansible.builtin.file:
        path: /opt/echo/victor-task-1
        state: directory

    - name: Template victor-task-1 config
      ansible.builtin.template:
        src: templates/victor-task-1.j2
        dest: /etc/echo/victor-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure fig-task-2 is present
      ansible.builtin.file:
        path: /opt/echo/fig-task-2
        state: directory

    - name: Template fig-task-2 config
      ansible.builtin.template:
        src: templates/fig-task-2.j2
        dest: /etc/echo/fig-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure sierra-task-3 is present
      ansible.builtin.file:
        path: /opt/echo/sierra-task-3
        state: directory

    - name: Template sierra-task-3 config
      ansible.builtin.template:
        src: templates/sierra-task-3.j2
        dest: /etc/echo/sierra-task-3.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart echo service
      ansible.builtin.service:
        name: echo
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:43Z
