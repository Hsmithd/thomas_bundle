# Play: Juliet - setup

- hosts: webservers
  become: true
  vars:
    app_name: "juliet_app"
    retry_count: 3

  tasks:
    - name: Ensure november-task-1 is present
      ansible.builtin.file:
        path: /opt/juliet/november-task-1
        state: directory

    - name: Template november-task-1 config
      ansible.builtin.template:
        src: templates/november-task-1.j2
        dest: /etc/juliet/november-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart juliet service
      ansible.builtin.service:
        name: juliet
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:43Z
