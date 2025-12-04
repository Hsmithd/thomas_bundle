# Play: Mike - setup

- hosts: webservers
  become: false
  vars:
    app_name: "mike_app"
    retry_count: 1

  tasks:
    - name: Ensure charlie-task-1 is present
      ansible.builtin.file:
        path: /opt/mike/charlie-task-1
        state: directory

    - name: Template charlie-task-1 config
      ansible.builtin.template:
        src: templates/charlie-task-1.j2
        dest: /etc/mike/charlie-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure kiwi-task-2 is present
      ansible.builtin.file:
        path: /opt/mike/kiwi-task-2
        state: directory

    - name: Template kiwi-task-2 config
      ansible.builtin.template:
        src: templates/kiwi-task-2.j2
        dest: /etc/mike/kiwi-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure tango-task-3 is present
      ansible.builtin.file:
        path: /opt/mike/tango-task-3
        state: directory

    - name: Template tango-task-3 config
      ansible.builtin.template:
        src: templates/tango-task-3.j2
        dest: /etc/mike/tango-task-3.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart mike service
      ansible.builtin.service:
        name: mike
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:44Z
