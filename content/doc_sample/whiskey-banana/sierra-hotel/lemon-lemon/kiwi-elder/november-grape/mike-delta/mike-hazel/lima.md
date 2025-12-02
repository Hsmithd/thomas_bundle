# Play: Lima - setup

- hosts: webservers
  become: true
  vars:
    app_name: "lima_app"
    retry_count: 5

  tasks:
    - name: Ensure bravo-task-1 is present
      ansible.builtin.file:
        path: /opt/lima/bravo-task-1
        state: directory

    - name: Template bravo-task-1 config
      ansible.builtin.template:
        src: templates/bravo-task-1.j2
        dest: /etc/lima/bravo-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure india-task-2 is present
      ansible.builtin.file:
        path: /opt/lima/india-task-2
        state: directory

    - name: Template india-task-2 config
      ansible.builtin.template:
        src: templates/india-task-2.j2
        dest: /etc/lima/india-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart lima service
      ansible.builtin.service:
        name: lima
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:43Z
