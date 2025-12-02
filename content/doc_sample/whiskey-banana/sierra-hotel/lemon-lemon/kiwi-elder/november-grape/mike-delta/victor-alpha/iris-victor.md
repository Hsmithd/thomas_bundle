# Play: Iris - setup

- hosts: webservers
  become: false
  vars:
    app_name: "iris_app"
    retry_count: 1

  tasks:
    - name: Ensure echo-task-1 is present
      ansible.builtin.file:
        path: /opt/iris/echo-task-1
        state: directory

    - name: Template echo-task-1 config
      ansible.builtin.template:
        src: templates/echo-task-1.j2
        dest: /etc/iris/echo-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure kiwi-task-2 is present
      ansible.builtin.file:
        path: /opt/iris/kiwi-task-2
        state: directory

    - name: Template kiwi-task-2 config
      ansible.builtin.template:
        src: templates/kiwi-task-2.j2
        dest: /etc/iris/kiwi-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure delta-task-3 is present
      ansible.builtin.file:
        path: /opt/iris/delta-task-3
        state: directory

    - name: Template delta-task-3 config
      ansible.builtin.template:
        src: templates/delta-task-3.j2
        dest: /etc/iris/delta-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart iris service
      ansible.builtin.service:
        name: iris
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:44Z
