# Play: Grape - setup

- hosts: webservers
  become: true
  vars:
    app_name: "grape_app"
    retry_count: 2

  tasks:
    - name: Ensure november-task-1 is present
      ansible.builtin.file:
        path: /opt/grape/november-task-1
        state: directory

    - name: Template november-task-1 config
      ansible.builtin.template:
        src: templates/november-task-1.j2
        dest: /etc/grape/november-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure bravo-task-2 is present
      ansible.builtin.file:
        path: /opt/grape/bravo-task-2
        state: directory

    - name: Template bravo-task-2 config
      ansible.builtin.template:
        src: templates/bravo-task-2.j2
        dest: /etc/grape/bravo-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure tango-task-3 is present
      ansible.builtin.file:
        path: /opt/grape/tango-task-3
        state: directory

    - name: Template tango-task-3 config
      ansible.builtin.template:
        src: templates/tango-task-3.j2
        dest: /etc/grape/tango-task-3.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure cherry-task-4 is present
      ansible.builtin.file:
        path: /opt/grape/cherry-task-4
        state: directory

    - name: Template cherry-task-4 config
      ansible.builtin.template:
        src: templates/cherry-task-4.j2
        dest: /etc/grape/cherry-task-4.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart grape service
      ansible.builtin.service:
        name: grape
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:44Z
