# Play: Grape - setup

- hosts: all
  become: false
  vars:
    app_name: "grape_app"
    retry_count: 3

  tasks:
    - name: Ensure date-task-1 is present
      ansible.builtin.file:
        path: /opt/grape/date-task-1
        state: directory

    - name: Template date-task-1 config
      ansible.builtin.template:
        src: templates/date-task-1.j2
        dest: /etc/grape/date-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure fig-task-2 is present
      ansible.builtin.file:
        path: /opt/grape/fig-task-2
        state: directory

    - name: Template fig-task-2 config
      ansible.builtin.template:
        src: templates/fig-task-2.j2
        dest: /etc/grape/fig-task-2.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart grape service
      ansible.builtin.service:
        name: grape
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:44Z
