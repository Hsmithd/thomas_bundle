# Play: Echo - setup

- hosts: db
  become: true
  vars:
    app_name: "echo_app"
    retry_count: 3

  tasks:
    - name: Ensure tango-task-1 is present
      ansible.builtin.file:
        path: /opt/echo/tango-task-1
        state: directory

    - name: Template tango-task-1 config
      ansible.builtin.template:
        src: templates/tango-task-1.j2
        dest: /etc/echo/tango-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart echo service
      ansible.builtin.service:
        name: echo
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:44Z
