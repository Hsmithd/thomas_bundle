# Play: Lima - setup

- hosts: all
  become: false
  vars:
    app_name: "lima_app"
    retry_count: 5

  tasks:
    - name: Ensure kilo-task-1 is present
      ansible.builtin.file:
        path: /opt/lima/kilo-task-1
        state: directory

    - name: Template kilo-task-1 config
      ansible.builtin.template:
        src: templates/kilo-task-1.j2
        dest: /etc/lima/kilo-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure grape-task-2 is present
      ansible.builtin.file:
        path: /opt/lima/grape-task-2
        state: directory

    - name: Template grape-task-2 config
      ansible.builtin.template:
        src: templates/grape-task-2.j2
        dest: /etc/lima/grape-task-2.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart lima service
      ansible.builtin.service:
        name: lima
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:44Z
