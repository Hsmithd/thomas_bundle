# Play: Uniform - setup

- hosts: webservers
  become: false
  vars:
    app_name: "uniform_app"
    retry_count: 3

  tasks:
    - name: Ensure banana-task-1 is present
      ansible.builtin.file:
        path: /opt/uniform/banana-task-1
        state: directory

    - name: Template banana-task-1 config
      ansible.builtin.template:
        src: templates/banana-task-1.j2
        dest: /etc/uniform/banana-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart uniform service
      ansible.builtin.service:
        name: uniform
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:44Z
