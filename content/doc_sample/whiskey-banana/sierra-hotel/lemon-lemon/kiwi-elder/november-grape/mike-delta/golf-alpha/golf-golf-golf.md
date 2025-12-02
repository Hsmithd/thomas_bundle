# Play: Golf - setup

- hosts: webservers
  become: true
  vars:
    app_name: "golf_app"
    retry_count: 5

  tasks:
    - name: Ensure mango-task-1 is present
      ansible.builtin.file:
        path: /opt/golf/mango-task-1
        state: directory

    - name: Template mango-task-1 config
      ansible.builtin.template:
        src: templates/mango-task-1.j2
        dest: /etc/golf/mango-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure victor-task-2 is present
      ansible.builtin.file:
        path: /opt/golf/victor-task-2
        state: directory

    - name: Template victor-task-2 config
      ansible.builtin.template:
        src: templates/victor-task-2.j2
        dest: /etc/golf/victor-task-2.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure yankee-task-3 is present
      ansible.builtin.file:
        path: /opt/golf/yankee-task-3
        state: directory

    - name: Template yankee-task-3 config
      ansible.builtin.template:
        src: templates/yankee-task-3.j2
        dest: /etc/golf/yankee-task-3.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart golf service
      ansible.builtin.service:
        name: golf
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:45Z
